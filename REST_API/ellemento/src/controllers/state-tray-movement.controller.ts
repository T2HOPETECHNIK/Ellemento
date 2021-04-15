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
  State,
  TrayMovement,
} from '../models';
import {StateRepository} from '../repositories';

export class StateTrayMovementController {
  constructor(
    @repository(StateRepository) protected stateRepository: StateRepository,
  ) { }

  @get('/states/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'Array of State has many TrayMovement',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(TrayMovement)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<TrayMovement>,
  ): Promise<TrayMovement[]> {
    return this.stateRepository.trayMovements(id).find(filter);
  }

  @post('/states/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'State model instance',
        content: {'application/json': {schema: getModelSchemaRef(TrayMovement)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof State.prototype.state_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {
            title: 'NewTrayMovementInState',
            exclude: ['tray_movement_id'],
            optional: ['stateId']
          }),
        },
      },
    }) trayMovement: Omit<TrayMovement, 'tray_movement_id'>,
  ): Promise<TrayMovement> {
    return this.stateRepository.trayMovements(id).create(trayMovement);
  }

  @patch('/states/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'State.TrayMovement PATCH success count',
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
    return this.stateRepository.trayMovements(id).patch(trayMovement, where);
  }

  @del('/states/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'State.TrayMovement DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(TrayMovement)) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.stateRepository.trayMovements(id).delete(where);
  }
}
