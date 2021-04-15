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
  LightHistory,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationLightHistoryController {
  constructor(
    @repository(LocationRepository) protected locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/light-histories', {
    responses: {
      '200': {
        description: 'Array of Location has many LightHistory',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(LightHistory)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<LightHistory>,
  ): Promise<LightHistory[]> {
    return this.locationRepository.lightHistories(id).find(filter);
  }

  @post('/locations/{id}/light-histories', {
    responses: {
      '200': {
        description: 'Location model instance',
        content: {'application/json': {schema: getModelSchemaRef(LightHistory)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Location.prototype.location_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LightHistory, {
            title: 'NewLightHistoryInLocation',
            exclude: ['light_history_id'],
            optional: ['locationId']
          }),
        },
      },
    }) lightHistory: Omit<LightHistory, 'light_history_id'>,
  ): Promise<LightHistory> {
    return this.locationRepository.lightHistories(id).create(lightHistory);
  }

  @patch('/locations/{id}/light-histories', {
    responses: {
      '200': {
        description: 'Location.LightHistory PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LightHistory, {partial: true}),
        },
      },
    })
    lightHistory: Partial<LightHistory>,
    @param.query.object('where', getWhereSchemaFor(LightHistory)) where?: Where<LightHistory>,
  ): Promise<Count> {
    return this.locationRepository.lightHistories(id).patch(lightHistory, where);
  }

  @del('/locations/{id}/light-histories', {
    responses: {
      '200': {
        description: 'Location.LightHistory DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(LightHistory)) where?: Where<LightHistory>,
  ): Promise<Count> {
    return this.locationRepository.lightHistories(id).delete(where);
  }
}
