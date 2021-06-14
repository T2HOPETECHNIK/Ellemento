import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  Location,
  LightHistory,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationLightHistoryController {
  constructor(
    @repository(LocationRepository)
    public locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/light-history', {
    responses: {
      '200': {
        description: 'LightHistory belonging to Location',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(LightHistory)},
          },
        },
      },
    },
  })
  async getLightHistory(
    @param.path.number('id') id: typeof Location.prototype.location_id,
  ): Promise<LightHistory> {
    return this.locationRepository.location(id);
  }
}
