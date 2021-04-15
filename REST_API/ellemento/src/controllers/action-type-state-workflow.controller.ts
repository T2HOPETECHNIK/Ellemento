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
  ActionType,
  StateWorkflow,
} from '../models';
import {ActionTypeRepository} from '../repositories';

export class ActionTypeStateWorkflowController {
  constructor(
    @repository(ActionTypeRepository) protected actionTypeRepository: ActionTypeRepository,
  ) { }

  @get('/action-types/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'Array of ActionType has many StateWorkflow',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(StateWorkflow)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<StateWorkflow>,
  ): Promise<StateWorkflow[]> {
    return this.actionTypeRepository.stateWorkflows(id).find(filter);
  }

  @post('/action-types/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'ActionType model instance',
        content: {'application/json': {schema: getModelSchemaRef(StateWorkflow)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof ActionType.prototype.action_type_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {
            title: 'NewStateWorkflowInActionType',
            exclude: ['state_type_id'],
            optional: ['actionTypeId']
          }),
        },
      },
    }) stateWorkflow: Omit<StateWorkflow, 'state_type_id'>,
  ): Promise<StateWorkflow> {
    return this.actionTypeRepository.stateWorkflows(id).create(stateWorkflow);
  }

  @patch('/action-types/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'ActionType.StateWorkflow PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {partial: true}),
        },
      },
    })
    stateWorkflow: Partial<StateWorkflow>,
    @param.query.object('where', getWhereSchemaFor(StateWorkflow)) where?: Where<StateWorkflow>,
  ): Promise<Count> {
    return this.actionTypeRepository.stateWorkflows(id).patch(stateWorkflow, where);
  }

  @del('/action-types/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'ActionType.StateWorkflow DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(StateWorkflow)) where?: Where<StateWorkflow>,
  ): Promise<Count> {
    return this.actionTypeRepository.stateWorkflows(id).delete(where);
  }
}
