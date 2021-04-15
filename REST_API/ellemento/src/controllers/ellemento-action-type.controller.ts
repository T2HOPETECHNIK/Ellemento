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
import {ActionType} from '../models';
import {ActionTypeRepository} from '../repositories';

export class EllementoActionTypeController {
  constructor(
    @repository(ActionTypeRepository)
    public actionTypeRepository : ActionTypeRepository,
  ) {}

  @post('/action-types')
  @response(200, {
    description: 'ActionType model instance',
    content: {'application/json': {schema: getModelSchemaRef(ActionType)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ActionType, {
            title: 'NewActionType',
            exclude: ['id'],
          }),
        },
      },
    })
    actionType: Omit<ActionType, 'id'>,
  ): Promise<ActionType> {
    return this.actionTypeRepository.create(actionType);
  }

  @get('/action-types/count')
  @response(200, {
    description: 'ActionType model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(ActionType) where?: Where<ActionType>,
  ): Promise<Count> {
    return this.actionTypeRepository.count(where);
  }

  @get('/action-types')
  @response(200, {
    description: 'Array of ActionType model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(ActionType, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(ActionType) filter?: Filter<ActionType>,
  ): Promise<ActionType[]> {
    return this.actionTypeRepository.find(filter);
  }

  @patch('/action-types')
  @response(200, {
    description: 'ActionType PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ActionType, {partial: true}),
        },
      },
    })
    actionType: ActionType,
    @param.where(ActionType) where?: Where<ActionType>,
  ): Promise<Count> {
    return this.actionTypeRepository.updateAll(actionType, where);
  }

  @get('/action-types/{id}')
  @response(200, {
    description: 'ActionType model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(ActionType, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(ActionType, {exclude: 'where'}) filter?: FilterExcludingWhere<ActionType>
  ): Promise<ActionType> {
    return this.actionTypeRepository.findById(id, filter);
  }

  @patch('/action-types/{id}')
  @response(204, {
    description: 'ActionType PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ActionType, {partial: true}),
        },
      },
    })
    actionType: ActionType,
  ): Promise<void> {
    await this.actionTypeRepository.updateById(id, actionType);
  }

  @put('/action-types/{id}')
  @response(204, {
    description: 'ActionType PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() actionType: ActionType,
  ): Promise<void> {
    await this.actionTypeRepository.replaceById(id, actionType);
  }

  @del('/action-types/{id}')
  @response(204, {
    description: 'ActionType DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.actionTypeRepository.deleteById(id);
  }
}
