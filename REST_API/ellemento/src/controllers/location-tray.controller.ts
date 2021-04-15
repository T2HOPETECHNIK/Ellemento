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
  Tray,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationTrayController {
  constructor(
    @repository(LocationRepository) protected locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/trays', {
    responses: {
      '200': {
        description: 'Array of Location has many Tray',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Tray)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Tray>,
  ): Promise<Tray[]> {
    return this.locationRepository.trays(id).find(filter);
  }

  @post('/locations/{id}/trays', {
    responses: {
      '200': {
        description: 'Location model instance',
        content: {'application/json': {schema: getModelSchemaRef(Tray)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Location.prototype.location_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Tray, {
            title: 'NewTrayInLocation',
            exclude: ['tray_id'],
            optional: ['locationId']
          }),
        },
      },
    }) tray: Omit<Tray, 'tray_id'>,
  ): Promise<Tray> {
    return this.locationRepository.trays(id).create(tray);
  }

  @patch('/locations/{id}/trays', {
    responses: {
      '200': {
        description: 'Location.Tray PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Tray, {partial: true}),
        },
      },
    })
    tray: Partial<Tray>,
    @param.query.object('where', getWhereSchemaFor(Tray)) where?: Where<Tray>,
  ): Promise<Count> {
    return this.locationRepository.trays(id).patch(tray, where);
  }

  @del('/locations/{id}/trays', {
    responses: {
      '200': {
        description: 'Location.Tray DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Tray)) where?: Where<Tray>,
  ): Promise<Count> {
    return this.locationRepository.trays(id).delete(where);
  }
}
