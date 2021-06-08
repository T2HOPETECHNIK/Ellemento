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
  StageErrorAction,
  ErrorType,
} from '../models';
import {StageErrorActionRepository} from '../repositories';

export class StageErrorActionErrorTypeController {
  constructor(
    @repository(StageErrorActionRepository) protected stageErrorActionRepository: StageErrorActionRepository,
  ) { }

  @get('/stage-error-actions/{id}/error-type', {
    responses: {
      '200': {
        description: 'StageErrorAction has one ErrorType',
        content: {
          'application/json': {
            schema: getModelSchemaRef(ErrorType),
          },
        },
      },
    },
  })
  async get(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<ErrorType>,
  ): Promise<ErrorType> {
    return this.stageErrorActionRepository.errorType(id).get(filter);
  }

  @post('/stage-error-actions/{id}/error-type', {
    responses: {
      '200': {
        description: 'StageErrorAction model instance',
        content: {'application/json': {schema: getModelSchemaRef(ErrorType)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof StageErrorAction.prototype.error_type_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ErrorType, {
            title: 'NewErrorTypeInStageErrorAction',
            exclude: ['error_type_id'],
            optional: ['stageErrorActionId']
          }),
        },
      },
    }) errorType: Omit<ErrorType, 'error_type_id'>,
  ): Promise<ErrorType> {
    return this.stageErrorActionRepository.errorType(id).create(errorType);
  }

  @patch('/stage-error-actions/{id}/error-type', {
    responses: {
      '200': {
        description: 'StageErrorAction.ErrorType PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(ErrorType, {partial: true}),
        },
      },
    })
    errorType: Partial<ErrorType>,
    @param.query.object('where', getWhereSchemaFor(ErrorType)) where?: Where<ErrorType>,
  ): Promise<Count> {
    return this.stageErrorActionRepository.errorType(id).patch(errorType, where);
  }

  @del('/stage-error-actions/{id}/error-type', {
    responses: {
      '200': {
        description: 'StageErrorAction.ErrorType DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(ErrorType)) where?: Where<ErrorType>,
  ): Promise<Count> {
    return this.stageErrorActionRepository.errorType(id).delete(where);
  }
}
