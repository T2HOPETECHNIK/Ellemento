import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  VentilationHistory,
  Location,
} from '../models';
import {VentilationHistoryRepository} from '../repositories';

export class VentilationHistoryLocationController {
  constructor(
    @repository(VentilationHistoryRepository)
    public ventilationHistoryRepository: VentilationHistoryRepository,
  ) { }

  @get('/ventilation-histories/{id}/location', {
    responses: {
      '200': {
        description: 'Location belonging to VentilationHistory',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Location)},
          },
        },
      },
    },
  })
  async getLocation(
    @param.path.number('id') id: typeof VentilationHistory.prototype.ventilation_history_id,
  ): Promise<Location> {
    return this.ventilationHistoryRepository.location(id);
  }
}
