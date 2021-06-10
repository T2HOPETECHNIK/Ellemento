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
  Transplanting,
} from '../models';
import {HistoryRepository} from '../repositories';

export class HistoryTransplantingController {
  constructor(
    @repository(HistoryRepository) protected historyRepository: HistoryRepository,
  ) { }

  @get('/histories/{id}/transplanting', {
    responses: {
      '200': {
        description: 'History has one Transplanting',
        content: {
          'application/json': {
            schema: getModelSchemaRef(Transplanting),
          },
        },
      },
    },
  })
  async get(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Transplanting>,
  ): Promise<Transplanting> {
    return this.historyRepository.transplanting(id).get(filter);
  }

  @post('/histories/{id}/transplanting', {
    responses: {
      '200': {
        description: 'History model instance',
        content: {'application/json': {schema: getModelSchemaRef(Transplanting)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof History.prototype.history_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Transplanting, {
            title: 'NewTransplantingInHistory',
            exclude: ['tray_action_table_id'],
            optional: ['historyId']
          }),
        },
      },
    }) transplanting: Omit<Transplanting, 'tray_action_table_id'>,
  ): Promise<Transplanting> {
    return this.historyRepository.transplanting(id).create(transplanting);
  }

  @patch('/histories/{id}/transplanting', {
    responses: {
      '200': {
        description: 'History.Transplanting PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Transplanting, {partial: true}),
        },
      },
    })
    transplanting: Partial<Transplanting>,
    @param.query.object('where', getWhereSchemaFor(Transplanting)) where?: Where<Transplanting>,
  ): Promise<Count> {
    return this.historyRepository.transplanting(id).patch(transplanting, where);
  }

  @del('/histories/{id}/transplanting', {
    responses: {
      '200': {
        description: 'History.Transplanting DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Transplanting)) where?: Where<Transplanting>,
  ): Promise<Count> {
    return this.historyRepository.transplanting(id).delete(where);
  }
}
