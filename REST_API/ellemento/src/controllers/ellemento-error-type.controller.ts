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
import {ErrorType} from '../models';
import {ErrorTypeRepository} from '../repositories';

export class EllementoErrorTypeController {
  constructor(
    @repository(ErrorTypeRepository)
    public errorTypeRepository : ErrorTypeRepository,
  ) {}

  @post('/error-types')
  @response(200, {
    description: 'ErrorType model instance',
    content: {'application/json': {schema: getModelSchemaRef(ErrorType)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ErrorType, {
            title: 'NewErrorType',
            exclude: ['id'],
          }),
        },
      },
    })
    errorType: Omit<ErrorType, 'id'>,
  ): Promise<ErrorType> {
    return this.errorTypeRepository.create(errorType);
  }

  @get('/error-types/count')
  @response(200, {
    description: 'ErrorType model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(ErrorType) where?: Where<ErrorType>,
  ): Promise<Count> {
    return this.errorTypeRepository.count(where);
  }

  @get('/error-types')
  @response(200, {
    description: 'Array of ErrorType model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(ErrorType, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(ErrorType) filter?: Filter<ErrorType>,
  ): Promise<ErrorType[]> {
    return this.errorTypeRepository.find(filter);
  }

  @patch('/error-types')
  @response(200, {
    description: 'ErrorType PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ErrorType, {partial: true}),
        },
      },
    })
    errorType: ErrorType,
    @param.where(ErrorType) where?: Where<ErrorType>,
  ): Promise<Count> {
    return this.errorTypeRepository.updateAll(errorType, where);
  }

  @get('/error-types/{id}')
  @response(200, {
    description: 'ErrorType model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(ErrorType, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(ErrorType, {exclude: 'where'}) filter?: FilterExcludingWhere<ErrorType>
  ): Promise<ErrorType> {
    return this.errorTypeRepository.findById(id, filter);
  }

  @patch('/error-types/{id}')
  @response(204, {
    description: 'ErrorType PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ErrorType, {partial: true}),
        },
      },
    })
    errorType: ErrorType,
  ): Promise<void> {
    await this.errorTypeRepository.updateById(id, errorType);
  }

  @put('/error-types/{id}')
  @response(204, {
    description: 'ErrorType PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() errorType: ErrorType,
  ): Promise<void> {
    await this.errorTypeRepository.replaceById(id, errorType);
  }

  @del('/error-types/{id}')
  @response(204, {
    description: 'ErrorType DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.errorTypeRepository.deleteById(id);
  }
}
