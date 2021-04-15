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
  Batch,
  State,
} from '../models';
import {BatchRepository} from '../repositories';

export class BatchStateController {
  constructor(
    @repository(BatchRepository) protected batchRepository: BatchRepository,
  ) { }

  @get('/batches/{id}/states', {
    responses: {
      '200': {
        description: 'Array of Batch has many State',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(State)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<State>,
  ): Promise<State[]> {
    return this.batchRepository.states(id).find(filter);
  }

  @post('/batches/{id}/states', {
    responses: {
      '200': {
        description: 'Batch model instance',
        content: {'application/json': {schema: getModelSchemaRef(State)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Batch.prototype.batch_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(State, {
            title: 'NewStateInBatch',
            exclude: ['state_id'],
            optional: ['batchId']
          }),
        },
      },
    }) state: Omit<State, 'state_id'>,
  ): Promise<State> {
    return this.batchRepository.states(id).create(state);
  }

  @patch('/batches/{id}/states', {
    responses: {
      '200': {
        description: 'Batch.State PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(State, {partial: true}),
        },
      },
    })
    state: Partial<State>,
    @param.query.object('where', getWhereSchemaFor(State)) where?: Where<State>,
  ): Promise<Count> {
    return this.batchRepository.states(id).patch(state, where);
  }

  @del('/batches/{id}/states', {
    responses: {
      '200': {
        description: 'Batch.State DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(State)) where?: Where<State>,
  ): Promise<Count> {
    return this.batchRepository.states(id).delete(where);
  }
}
