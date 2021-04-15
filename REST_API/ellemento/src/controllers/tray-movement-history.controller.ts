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
  TrayMovement,
  History,
} from '../models';
import {TrayMovementRepository} from '../repositories';

export class TrayMovementHistoryController {
  constructor(
    @repository(TrayMovementRepository) protected trayMovementRepository: TrayMovementRepository,
  ) { }

  @get('/tray-movements/{id}/histories', {
    responses: {
      '200': {
        description: 'Array of TrayMovement has many History',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(History)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<History>,
  ): Promise<History[]> {
    return this.trayMovementRepository.histories(id).find(filter);
  }

  @post('/tray-movements/{id}/histories', {
    responses: {
      '200': {
        description: 'TrayMovement model instance',
        content: {'application/json': {schema: getModelSchemaRef(History)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof TrayMovement.prototype.tray_movement_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(History, {
            title: 'NewHistoryInTrayMovement',
            exclude: ['history_id'],
            optional: ['trayMovementId']
          }),
        },
      },
    }) history: Omit<History, 'history_id'>,
  ): Promise<History> {
    return this.trayMovementRepository.histories(id).create(history);
  }

  @patch('/tray-movements/{id}/histories', {
    responses: {
      '200': {
        description: 'TrayMovement.History PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(History, {partial: true}),
        },
      },
    })
    history: Partial<History>,
    @param.query.object('where', getWhereSchemaFor(History)) where?: Where<History>,
  ): Promise<Count> {
    return this.trayMovementRepository.histories(id).patch(history, where);
  }

  @del('/tray-movements/{id}/histories', {
    responses: {
      '200': {
        description: 'TrayMovement.History DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(History)) where?: Where<History>,
  ): Promise<Count> {
    return this.trayMovementRepository.histories(id).delete(where);
  }
}
