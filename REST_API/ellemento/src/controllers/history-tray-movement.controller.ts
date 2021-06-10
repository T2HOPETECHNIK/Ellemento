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
  TrayMovement,
} from '../models';
import {HistoryRepository} from '../repositories';

export class HistoryTrayMovementController {
  constructor(
    @repository(HistoryRepository) protected historyRepository: HistoryRepository,
  ) { }

  @get('/histories/{id}/tray-movement', {
    responses: {
      '200': {
        description: 'History has one TrayMovement',
        content: {
          'application/json': {
            schema: getModelSchemaRef(TrayMovement),
          },
        },
      },
    },
  })
  async get(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<TrayMovement>,
  ): Promise<TrayMovement> {
    return this.historyRepository.trayMovement(id).get(filter);
  }

  @post('/histories/{id}/tray-movement', {
    responses: {
      '200': {
        description: 'History model instance',
        content: {'application/json': {schema: getModelSchemaRef(TrayMovement)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof History.prototype.history_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {
            title: 'NewTrayMovementInHistory',
            exclude: ['tray_movement_id'],
            optional: ['tray_action_table_id']
          }),
        },
      },
    }) trayMovement: Omit<TrayMovement, 'tray_movement_id'>,
  ): Promise<TrayMovement> {
    return this.historyRepository.trayMovement(id).create(trayMovement);
  }

  @patch('/histories/{id}/tray-movement', {
    responses: {
      '200': {
        description: 'History.TrayMovement PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {partial: true}),
        },
      },
    })
    trayMovement: Partial<TrayMovement>,
    @param.query.object('where', getWhereSchemaFor(TrayMovement)) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.historyRepository.trayMovement(id).patch(trayMovement, where);
  }

  @del('/histories/{id}/tray-movement', {
    responses: {
      '200': {
        description: 'History.TrayMovement DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(TrayMovement)) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.historyRepository.trayMovement(id).delete(where);
  }
}
