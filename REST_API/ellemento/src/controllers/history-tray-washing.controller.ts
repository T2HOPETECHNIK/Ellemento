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
  TrayWashing,
} from '../models';
import {HistoryRepository} from '../repositories';

export class HistoryTrayWashingController {
  constructor(
    @repository(HistoryRepository) protected historyRepository: HistoryRepository,
  ) { }

  @get('/histories/{id}/tray-washing', {
    responses: {
      '200': {
        description: 'History has one TrayWashing',
        content: {
          'application/json': {
            schema: getModelSchemaRef(TrayWashing),
          },
        },
      },
    },
  })
  async get(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<TrayWashing>,
  ): Promise<TrayWashing> {
    return this.historyRepository.trayWashing(id).get(filter);
  }

  @post('/histories/{id}/tray-washing', {
    responses: {
      '200': {
        description: 'History model instance',
        content: {'application/json': {schema: getModelSchemaRef(TrayWashing)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof History.prototype.history_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayWashing, {
            title: 'NewTrayWashingInHistory',
            exclude: ['tray_action_table_id'],
            optional: ['historyId']
          }),
        },
      },
    }) trayWashing: Omit<TrayWashing, 'tray_action_table_id'>,
  ): Promise<TrayWashing> {
    return this.historyRepository.trayWashing(id).create(trayWashing);
  }

  @patch('/histories/{id}/tray-washing', {
    responses: {
      '200': {
        description: 'History.TrayWashing PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayWashing, {partial: true}),
        },
      },
    })
    trayWashing: Partial<TrayWashing>,
    @param.query.object('where', getWhereSchemaFor(TrayWashing)) where?: Where<TrayWashing>,
  ): Promise<Count> {
    return this.historyRepository.trayWashing(id).patch(trayWashing, where);
  }

  @del('/histories/{id}/tray-washing', {
    responses: {
      '200': {
        description: 'History.TrayWashing DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(TrayWashing)) where?: Where<TrayWashing>,
  ): Promise<Count> {
    return this.historyRepository.trayWashing(id).delete(where);
  }
}
