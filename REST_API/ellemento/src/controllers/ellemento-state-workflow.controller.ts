import {
  Count,
  CountSchema,
  Filter,
  FilterExcludingWhere,
  repository,
  Where,
} from '@loopback/repository';
import {
  post,
  param,
  get,
  getModelSchemaRef,
  patch,
  put,
  del,
  requestBody,
  response,
} from '@loopback/rest';
import {StateWorkflow} from '../models';
import {StateWorkflowRepository} from '../repositories';

export class EllementoStateWorkflowController {
  constructor(
    @repository(StateWorkflowRepository)
    public stateWorkflowRepository : StateWorkflowRepository,
  ) {}

  @post('/state-workflows')
  @response(200, {
    description: 'StateWorkflow model instance',
    content: {'application/json': {schema: getModelSchemaRef(StateWorkflow)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {
            title: 'NewStateWorkflow',
            exclude: ['id'],
          }),
        },
      },
    })
    stateWorkflow: Omit<StateWorkflow, 'id'>,
  ): Promise<StateWorkflow> {
    return this.stateWorkflowRepository.create(stateWorkflow);
  }

  @get('/state-workflows/count')
  @response(200, {
    description: 'StateWorkflow model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(StateWorkflow) where?: Where<StateWorkflow>,
  ): Promise<Count> {
    return this.stateWorkflowRepository.count(where);
  }

  @get('/state-workflows')
  @response(200, {
    description: 'Array of StateWorkflow model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(StateWorkflow, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(StateWorkflow) filter?: Filter<StateWorkflow>,
  ): Promise<StateWorkflow[]> {
    return this.stateWorkflowRepository.find(filter);
  }

  @patch('/state-workflows')
  @response(200, {
    description: 'StateWorkflow PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {partial: true}),
        },
      },
    })
    stateWorkflow: StateWorkflow,
    @param.where(StateWorkflow) where?: Where<StateWorkflow>,
  ): Promise<Count> {
    return this.stateWorkflowRepository.updateAll(stateWorkflow, where);
  }

  @get('/state-workflows/{id}')
  @response(200, {
    description: 'StateWorkflow model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(StateWorkflow, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(StateWorkflow, {exclude: 'where'}) filter?: FilterExcludingWhere<StateWorkflow>
  ): Promise<StateWorkflow> {
    return this.stateWorkflowRepository.findById(id, filter);
  }

  @patch('/state-workflows/{id}')
  @response(204, {
    description: 'StateWorkflow PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(StateWorkflow, {partial: true}),
        },
      },
    })
    stateWorkflow: StateWorkflow,
  ): Promise<void> {
    await this.stateWorkflowRepository.updateById(id, stateWorkflow);
  }

  @put('/state-workflows/{id}')
  @response(204, {
    description: 'StateWorkflow PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() stateWorkflow: StateWorkflow,
  ): Promise<void> {
    await this.stateWorkflowRepository.replaceById(id, stateWorkflow);
  }

  @del('/state-workflows/{id}')
  @response(204, {
    description: 'StateWorkflow DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.stateWorkflowRepository.deleteById(id);
  }
}
