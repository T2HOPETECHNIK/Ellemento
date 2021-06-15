import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  WaterHistory,
  Location,
} from '../models';
import {WaterHistoryRepository} from '../repositories';

export class WaterHistoryLocationController {
  constructor(
    @repository(WaterHistoryRepository)
    public waterHistoryRepository: WaterHistoryRepository,
  ) { }

  @get('/water-histories/{id}/location', {
    responses: {
      '200': {
        description: 'Location belonging to WaterHistory',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Location)},
          },
        },
      },
    },
  })
  async getLocation(
    @param.path.number('id') id: typeof WaterHistory.prototype.water_history_id,
  ): Promise<Location> {
    return this.waterHistoryRepository.location(id);
  }
}
