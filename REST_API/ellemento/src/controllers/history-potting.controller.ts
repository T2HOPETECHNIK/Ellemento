import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  History,
  Potting,
} from '../models';
import {HistoryRepository} from '../repositories';

export class HistoryPottingController {
  constructor(
    @repository(HistoryRepository)
    public historyRepository: HistoryRepository,
  ) { }

  @get('/histories/{id}/potting', {
    responses: {
      '200': {
        description: 'Potting belonging to History',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Potting)},
          },
        },
      },
    },
  })
  async getPotting(
    @param.path.number('id') id: typeof History.prototype.history_id,
  ): Promise<Potting> {
    return this.historyRepository.trayActionTableId(id);
  }
}
