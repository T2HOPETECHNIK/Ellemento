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
import {LightHistory} from '../models';
import {LightHistoryRepository} from '../repositories';

export class EllementoLightHistoryController {
  constructor(
    @repository(LightHistoryRepository)
    public lightHistoryRepository : LightHistoryRepository,
  ) {}

  @post('/light-histories')
  @response(200, {
    description: 'LightHistory model instance',
    content: {'application/json': {schema: getModelSchemaRef(LightHistory)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LightHistory, {
            title: 'NewLightHistory',
            exclude: ['id'],
          }),
        },
      },
    })
    lightHistory: Omit<LightHistory, 'id'>,
  ): Promise<LightHistory> {
    return this.lightHistoryRepository.create(lightHistory);
  }

  @get('/light-histories/count')
  @response(200, {
    description: 'LightHistory model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(LightHistory) where?: Where<LightHistory>,
  ): Promise<Count> {
    return this.lightHistoryRepository.count(where);
  }

  @get('/light-histories')
  @response(200, {
    description: 'Array of LightHistory model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(LightHistory, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(LightHistory) filter?: Filter<LightHistory>,
  ): Promise<LightHistory[]> {
    return this.lightHistoryRepository.find(filter);
  }

  @patch('/light-histories')
  @response(200, {
    description: 'LightHistory PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LightHistory, {partial: true}),
        },
      },
    })
    lightHistory: LightHistory,
    @param.where(LightHistory) where?: Where<LightHistory>,
  ): Promise<Count> {
    return this.lightHistoryRepository.updateAll(lightHistory, where);
  }

  @get('/light-histories/{id}')
  @response(200, {
    description: 'LightHistory model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(LightHistory, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(LightHistory, {exclude: 'where'}) filter?: FilterExcludingWhere<LightHistory>
  ): Promise<LightHistory> {
    return this.lightHistoryRepository.findById(id, filter);
  }

  @patch('/light-histories/{id}')
  @response(204, {
    description: 'LightHistory PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LightHistory, {partial: true}),
        },
      },
    })
    lightHistory: LightHistory,
  ): Promise<void> {
    await this.lightHistoryRepository.updateById(id, lightHistory);
  }

  @put('/light-histories/{id}')
  @response(204, {
    description: 'LightHistory PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() lightHistory: LightHistory,
  ): Promise<void> {
    await this.lightHistoryRepository.replaceById(id, lightHistory);
  }

  @del('/light-histories/{id}')
  @response(204, {
    description: 'LightHistory DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.lightHistoryRepository.deleteById(id);
  }
}
