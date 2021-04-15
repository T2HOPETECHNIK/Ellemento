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
import {WaterHistory} from '../models';
import {WaterHistoryRepository} from '../repositories';

export class EllementoWaterHistoryController {
  constructor(
    @repository(WaterHistoryRepository)
    public waterHistoryRepository : WaterHistoryRepository,
  ) {}

  @post('/water-histories')
  @response(200, {
    description: 'WaterHistory model instance',
    content: {'application/json': {schema: getModelSchemaRef(WaterHistory)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(WaterHistory, {
            title: 'NewWaterHistory',
            exclude: ['id'],
          }),
        },
      },
    })
    waterHistory: Omit<WaterHistory, 'id'>,
  ): Promise<WaterHistory> {
    return this.waterHistoryRepository.create(waterHistory);
  }

  @get('/water-histories/count')
  @response(200, {
    description: 'WaterHistory model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(WaterHistory) where?: Where<WaterHistory>,
  ): Promise<Count> {
    return this.waterHistoryRepository.count(where);
  }

  @get('/water-histories')
  @response(200, {
    description: 'Array of WaterHistory model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(WaterHistory, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(WaterHistory) filter?: Filter<WaterHistory>,
  ): Promise<WaterHistory[]> {
    return this.waterHistoryRepository.find(filter);
  }

  @patch('/water-histories')
  @response(200, {
    description: 'WaterHistory PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(WaterHistory, {partial: true}),
        },
      },
    })
    waterHistory: WaterHistory,
    @param.where(WaterHistory) where?: Where<WaterHistory>,
  ): Promise<Count> {
    return this.waterHistoryRepository.updateAll(waterHistory, where);
  }

  @get('/water-histories/{id}')
  @response(200, {
    description: 'WaterHistory model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(WaterHistory, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(WaterHistory, {exclude: 'where'}) filter?: FilterExcludingWhere<WaterHistory>
  ): Promise<WaterHistory> {
    return this.waterHistoryRepository.findById(id, filter);
  }

  @patch('/water-histories/{id}')
  @response(204, {
    description: 'WaterHistory PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(WaterHistory, {partial: true}),
        },
      },
    })
    waterHistory: WaterHistory,
  ): Promise<void> {
    await this.waterHistoryRepository.updateById(id, waterHistory);
  }

  @put('/water-histories/{id}')
  @response(204, {
    description: 'WaterHistory PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() waterHistory: WaterHistory,
  ): Promise<void> {
    await this.waterHistoryRepository.replaceById(id, waterHistory);
  }

  @del('/water-histories/{id}')
  @response(204, {
    description: 'WaterHistory DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.waterHistoryRepository.deleteById(id);
  }
}
