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
  History,
} from '../models';
import {BatchRepository} from '../repositories';

export class BatchHistoryController {
  constructor(
    @repository(BatchRepository) protected batchRepository: BatchRepository,
  ) { }

  @get('/batches/{id}/histories', {
    responses: {
      '200': {
        description: 'Array of Batch has many History',
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
    return this.batchRepository.histories(id).find(filter);
  }

  @post('/batches/{id}/histories', {
    responses: {
      '200': {
        description: 'Batch model instance',
        content: {'application/json': {schema: getModelSchemaRef(History)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Batch.prototype.batch_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(History, {
            title: 'NewHistoryInBatch',
            exclude: ['history_id'],
            optional: ['batchId']
          }),
        },
      },
    }) history: Omit<History, 'history_id'>,
  ): Promise<History> {
    return this.batchRepository.histories(id).create(history);
  }

  @patch('/batches/{id}/histories', {
    responses: {
      '200': {
        description: 'Batch.History PATCH success count',
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
    return this.batchRepository.histories(id).patch(history, where);
  }

  @del('/batches/{id}/histories', {
    responses: {
      '200': {
        description: 'Batch.History DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(History)) where?: Where<History>,
  ): Promise<Count> {
    return this.batchRepository.histories(id).delete(where);
  }
}
