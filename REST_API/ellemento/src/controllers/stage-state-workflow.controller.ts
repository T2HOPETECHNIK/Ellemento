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
  Stage,
  StateWorkflow,
} from '../models';
import {StageRepository} from '../repositories';

export class StageStateWorkflowController {
  constructor(
    @repository(StageRepository) protected stageRepository: StageRepository,
  ) { }

  @get('/stages/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'Array of Stage has many StateWorkflow',
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
    return this.stageRepository.stateWorkflows(id).find(filter);
  }

  @post('/stages/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'Stage model instance',
        content: {'application/json': {schema: getModelSchemaRef(StateWorkflow)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Stage.prototype.stage_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {
            title: 'NewStateWorkflowInStage',
            exclude: ['state_type_id'],
            optional: ['stageId']
          }),
        },
      },
    }) stateWorkflow: Omit<StateWorkflow, 'state_type_id'>,
  ): Promise<StateWorkflow> {
    return this.stageRepository.stateWorkflows(id).create(stateWorkflow);
  }

  @patch('/stages/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'Stage.StateWorkflow PATCH success count',
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
    return this.stageRepository.stateWorkflows(id).patch(stateWorkflow, where);
  }

  @del('/stages/{id}/state-workflows', {
    responses: {
      '200': {
        description: 'Stage.StateWorkflow DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(StateWorkflow)) where?: Where<StateWorkflow>,
  ): Promise<Count> {
    return this.stageRepository.stateWorkflows(id).delete(where);
  }
}
