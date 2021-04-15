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
  Location,
  WaterHistory,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationWaterHistoryController {
  constructor(
    @repository(LocationRepository) protected locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/water-histories', {
    responses: {
      '200': {
        description: 'Array of Location has many WaterHistory',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(WaterHistory)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<WaterHistory>,
  ): Promise<WaterHistory[]> {
    return this.locationRepository.waterHistories(id).find(filter);
  }

  @post('/locations/{id}/water-histories', {
    responses: {
      '200': {
        description: 'Location model instance',
        content: {'application/json': {schema: getModelSchemaRef(WaterHistory)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Location.prototype.location_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(WaterHistory, {
            title: 'NewWaterHistoryInLocation',
            exclude: ['water_history_id'],
            optional: ['locationId']
          }),
        },
      },
    }) waterHistory: Omit<WaterHistory, 'water_history_id'>,
  ): Promise<WaterHistory> {
    return this.locationRepository.waterHistories(id).create(waterHistory);
  }

  @patch('/locations/{id}/water-histories', {
    responses: {
      '200': {
        description: 'Location.WaterHistory PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(WaterHistory, {partial: true}),
        },
      },
    })
    waterHistory: Partial<WaterHistory>,
    @param.query.object('where', getWhereSchemaFor(WaterHistory)) where?: Where<WaterHistory>,
  ): Promise<Count> {
    return this.locationRepository.waterHistories(id).patch(waterHistory, where);
  }

  @del('/locations/{id}/water-histories', {
    responses: {
      '200': {
        description: 'Location.WaterHistory DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(WaterHistory)) where?: Where<WaterHistory>,
  ): Promise<Count> {
    return this.locationRepository.waterHistories(id).delete(where);
  }
}
