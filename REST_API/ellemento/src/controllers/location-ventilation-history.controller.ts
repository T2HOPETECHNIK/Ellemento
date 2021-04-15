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
  VentilationHistory,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationVentilationHistoryController {
  constructor(
    @repository(LocationRepository) protected locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/ventilation-histories', {
    responses: {
      '200': {
        description: 'Array of Location has many VentilationHistory',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(VentilationHistory)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<VentilationHistory>,
  ): Promise<VentilationHistory[]> {
    return this.locationRepository.ventilationHistories(id).find(filter);
  }

  @post('/locations/{id}/ventilation-histories', {
    responses: {
      '200': {
        description: 'Location model instance',
        content: {'application/json': {schema: getModelSchemaRef(VentilationHistory)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Location.prototype.location_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(VentilationHistory, {
            title: 'NewVentilationHistoryInLocation',
            exclude: ['ventilation_history_id'],
            optional: ['locationId']
          }),
        },
      },
    }) ventilationHistory: Omit<VentilationHistory, 'ventilation_history_id'>,
  ): Promise<VentilationHistory> {
    return this.locationRepository.ventilationHistories(id).create(ventilationHistory);
  }

  @patch('/locations/{id}/ventilation-histories', {
    responses: {
      '200': {
        description: 'Location.VentilationHistory PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(VentilationHistory, {partial: true}),
        },
      },
    })
    ventilationHistory: Partial<VentilationHistory>,
    @param.query.object('where', getWhereSchemaFor(VentilationHistory)) where?: Where<VentilationHistory>,
  ): Promise<Count> {
    return this.locationRepository.ventilationHistories(id).patch(ventilationHistory, where);
  }

  @del('/locations/{id}/ventilation-histories', {
    responses: {
      '200': {
        description: 'Location.VentilationHistory DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(VentilationHistory)) where?: Where<VentilationHistory>,
  ): Promise<Count> {
    return this.locationRepository.ventilationHistories(id).delete(where);
  }
}
