import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  LightHistory,
  Location,
} from '../models';
import {LightHistoryRepository} from '../repositories';

export class LightHistoryLocationController {
  constructor(
    @repository(LightHistoryRepository)
    public lightHistoryRepository: LightHistoryRepository,
  ) { }

  @get('/light-histories/{id}/location', {
    responses: {
      '200': {
        description: 'Location belonging to LightHistory',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Location)},
          },
        },
      },
    },
  })
  async getLocation(
    @param.path.number('id') id: typeof LightHistory.prototype.light_history_id,
  ): Promise<Location> {
    return this.lightHistoryRepository.location(id);
  }
}
