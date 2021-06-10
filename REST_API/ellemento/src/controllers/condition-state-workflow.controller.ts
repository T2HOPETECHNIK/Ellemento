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
  Condition,
  StateWorkflow,
} from '../models';
import {ConditionRepository} from '../repositories';

export class ConditionStateWorkflowController {
  constructor(
    @repository(ConditionRepository) protected conditionRepository: ConditionRepository,
  ) { }

  @get('/conditions/{id}/state-workflow', {
    responses: {
      '200': {
        description: 'Condition has one StateWorkflow',
        content: {
          'application/json': {
            schema: getModelSchemaRef(StateWorkflow),
          },
        },
      },
    },
  })
  async get(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<StateWorkflow>,
  ): Promise<StateWorkflow> {
    return this.conditionRepository.stateWorkflow(id).get(filter);
  }

  @post('/conditions/{id}/state-workflow', {
    responses: {
      '200': {
        description: 'Condition model instance',
        content: {'application/json': {schema: getModelSchemaRef(StateWorkflow)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Condition.prototype.condition_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {
            title: 'NewStateWorkflowInCondition',
            exclude: ['state_type_id'],
            optional: ['condition_id']
          }),
        },
      },
    }) stateWorkflow: Omit<StateWorkflow, 'state_type_id'>,
  ): Promise<StateWorkflow> {
    return this.conditionRepository.stateWorkflow(id).create(stateWorkflow);
  }

  @patch('/conditions/{id}/state-workflow', {
    responses: {
      '200': {
        description: 'Condition.StateWorkflow PATCH success count',
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
    return this.conditionRepository.stateWorkflow(id).patch(stateWorkflow, where);
  }

  @del('/conditions/{id}/state-workflow', {
    responses: {
      '200': {
        description: 'Condition.StateWorkflow DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(StateWorkflow)) where?: Where<StateWorkflow>,
  ): Promise<Count> {
    return this.conditionRepository.stateWorkflow(id).delete(where);
  }
}
