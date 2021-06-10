import {
  Count,
  CountSchema,
  Filter,
  repository,
  Where,
} from '@loopback/repository';
import {
  del,
  get,
  getModelSchemaRef,
  getWhereSchemaFor,
  param,
  patch,
  post,
  requestBody,
} from '@loopback/rest';
import {
  History,
  Potting,
} from '../models';
import {HistoryRepository} from '../repositories';

export class HistoryPottingController {
  constructor(
    @repository(HistoryRepository) protected historyRepository: HistoryRepository,
  ) { }

  @get('/histories/{id}/potting', {
    responses: {
      '200': {
        description: 'History has one Potting',
        content: {
          'application/json': {
            schema: getModelSchemaRef(Potting),
          },
        },
      },
    },
  })
  async get(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Potting>,
  ): Promise<Potting> {
    return this.historyRepository.potting(id).get(filter);
  }

  @post('/histories/{id}/potting', {
    responses: {
      '200': {
        description: 'History model instance',
        content: {'application/json': {schema: getModelSchemaRef(Potting)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof History.prototype.history_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Potting, {
            title: 'NewPottingInHistory',
            exclude: ['tray_action_table_id'],
            optional: ['tray_action_table_id']
          }),
        },
      },
    }) potting: Omit<Potting, 'tray_action_table_id'>,
  ): Promise<Potting> {
    return this.historyRepository.potting(id).create(potting);
  }

  @patch('/histories/{id}/potting', {
    responses: {
      '200': {
        description: 'History.Potting PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Potting, {partial: true}),
        },
      },
    })
    potting: Partial<Potting>,
    @param.query.object('where', getWhereSchemaFor(Potting)) where?: Where<Potting>,
  ): Promise<Count> {
    return this.historyRepository.potting(id).patch(potting, where);
  }

  @del('/histories/{id}/potting', {
    responses: {
      '200': {
        description: 'History.Potting DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Potting)) where?: Where<Potting>,
  ): Promise<Count> {
    return this.historyRepository.potting(id).delete(where);
  }
}
