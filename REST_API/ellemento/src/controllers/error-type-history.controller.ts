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
  ErrorType,
  History,
} from '../models';
import {ErrorTypeRepository} from '../repositories';

export class ErrorTypeHistoryController {
  constructor(
    @repository(ErrorTypeRepository) protected errorTypeRepository: ErrorTypeRepository,
  ) { }

  @get('/error-types/{id}/histories', {
    responses: {
      '200': {
        description: 'Array of ErrorType has many History',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(History)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<History>,
  ): Promise<History[]> {
    return this.errorTypeRepository.histories(id).find(filter);
  }

  @post('/error-types/{id}/histories', {
    responses: {
      '200': {
        description: 'ErrorType model instance',
        content: {'application/json': {schema: getModelSchemaRef(History)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof ErrorType.prototype.error_type_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(History, {
            title: 'NewHistoryInErrorType',
            exclude: ['history_id'],
            optional: ['errorTypeId']
          }),
        },
      },
    }) history: Omit<History, 'history_id'>,
  ): Promise<History> {
    return this.errorTypeRepository.histories(id).create(history);
  }

  @patch('/error-types/{id}/histories', {
    responses: {
      '200': {
        description: 'ErrorType.History PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(History, {partial: true}),
        },
      },
    })
    history: Partial<History>,
    @param.query.object('where', getWhereSchemaFor(History)) where?: Where<History>,
  ): Promise<Count> {
    return this.errorTypeRepository.histories(id).patch(history, where);
  }

  @del('/error-types/{id}/histories', {
    responses: {
      '200': {
        description: 'ErrorType.History DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(History)) where?: Where<History>,
  ): Promise<Count> {
    return this.errorTypeRepository.histories(id).delete(where);
  }
}
