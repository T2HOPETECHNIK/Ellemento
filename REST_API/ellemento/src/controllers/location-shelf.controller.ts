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
  Shelf,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationShelfController {
  constructor(
    @repository(LocationRepository)
    public locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/shelf', {
    responses: {
      '200': {
        description: 'Shelf belonging to Location',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Shelf)},
          },
        },
      },
    },
  })
  async getShelf(
    @param.path.number('id') id: typeof Location.prototype.location_id,
  ): Promise<Shelf> {
    return this.locationRepository.shelf(id);
  }
}
