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
  StateWorkflow,
  State,
} from '../models';
import {StateWorkflowRepository} from '../repositories';

export class StateWorkflowStateController {
  constructor(
    @repository(StateWorkflowRepository) protected stateWorkflowRepository: StateWorkflowRepository,
  ) { }

  @get('/state-workflows/{id}/states', {
    responses: {
      '200': {
        description: 'Array of StateWorkflow has many State',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(State)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<State>,
  ): Promise<State[]> {
    return this.stateWorkflowRepository.states(id).find(filter);
  }

  @post('/state-workflows/{id}/states', {
    responses: {
      '200': {
        description: 'StateWorkflow model instance',
        content: {'application/json': {schema: getModelSchemaRef(State)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof StateWorkflow.prototype.state_type_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(State, {
            title: 'NewStateInStateWorkflow',
            exclude: ['state_id'],
            optional: ['state_type_id']
          }),
        },
      },
    }) state: Omit<State, 'state_id'>,
  ): Promise<State> {
    return this.stateWorkflowRepository.states(id).create(state);
  }

  @patch('/state-workflows/{id}/states', {
    responses: {
      '200': {
        description: 'StateWorkflow.State PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(State, {partial: true}),
        },
      },
    })
    state: Partial<State>,
    @param.query.object('where', getWhereSchemaFor(State)) where?: Where<State>,
  ): Promise<Count> {
    return this.stateWorkflowRepository.states(id).patch(state, where);
  }

  @del('/state-workflows/{id}/states', {
    responses: {
      '200': {
        description: 'StateWorkflow.State DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(State)) where?: Where<State>,
  ): Promise<Count> {
    return this.stateWorkflowRepository.states(id).delete(where);
  }
}
