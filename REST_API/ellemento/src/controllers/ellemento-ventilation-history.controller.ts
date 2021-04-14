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
import {VentilationHistory} from '../models';
import {VentilationHistoryRepository} from '../repositories';

export class EllementoVentilationHistoryController {
  constructor(
    @repository(VentilationHistoryRepository)
    public ventilationHistoryRepository : VentilationHistoryRepository,
  ) {}

  @post('/ventilation-histories')
  @response(200, {
    description: 'VentilationHistory model instance',
    content: {'application/json': {schema: getModelSchemaRef(VentilationHistory)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(VentilationHistory, {
            title: 'NewVentilationHistory',
            exclude: ['id'],
          }),
        },
      },
    })
    ventilationHistory: Omit<VentilationHistory, 'id'>,
  ): Promise<VentilationHistory> {
    return this.ventilationHistoryRepository.create(ventilationHistory);
  }

  @get('/ventilation-histories/count')
  @response(200, {
    description: 'VentilationHistory model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(VentilationHistory) where?: Where<VentilationHistory>,
  ): Promise<Count> {
    return this.ventilationHistoryRepository.count(where);
  }

  @get('/ventilation-histories')
  @response(200, {
    description: 'Array of VentilationHistory model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(VentilationHistory, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(VentilationHistory) filter?: Filter<VentilationHistory>,
  ): Promise<VentilationHistory[]> {
    return this.ventilationHistoryRepository.find(filter);
  }

  @patch('/ventilation-histories')
  @response(200, {
    description: 'VentilationHistory PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(VentilationHistory, {partial: true}),
        },
      },
    })
    ventilationHistory: VentilationHistory,
    @param.where(VentilationHistory) where?: Where<VentilationHistory>,
  ): Promise<Count> {
    return this.ventilationHistoryRepository.updateAll(ventilationHistory, where);
  }

  @get('/ventilation-histories/{id}')
  @response(200, {
    description: 'VentilationHistory model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(VentilationHistory, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(VentilationHistory, {exclude: 'where'}) filter?: FilterExcludingWhere<VentilationHistory>
  ): Promise<VentilationHistory> {
    return this.ventilationHistoryRepository.findById(id, filter);
  }

  @patch('/ventilation-histories/{id}')
  @response(204, {
    description: 'VentilationHistory PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(VentilationHistory, {partial: true}),
        },
      },
    })
    ventilationHistory: VentilationHistory,
  ): Promise<void> {
    await this.ventilationHistoryRepository.updateById(id, ventilationHistory);
  }

  @put('/ventilation-histories/{id}')
  @response(204, {
    description: 'VentilationHistory PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() ventilationHistory: VentilationHistory,
  ): Promise<void> {
    await this.ventilationHistoryRepository.replaceById(id, ventilationHistory);
  }

  @del('/ventilation-histories/{id}')
  @response(204, {
    description: 'VentilationHistory DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.ventilationHistoryRepository.deleteById(id);
  }
}
