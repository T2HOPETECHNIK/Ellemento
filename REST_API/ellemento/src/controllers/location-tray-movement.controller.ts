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
  TrayMovement,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationTrayMovementController {
  constructor(
    @repository(LocationRepository) protected locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'Array of Location has many TrayMovement',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(TrayMovement)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<TrayMovement>,
  ): Promise<TrayMovement[]> {
    return this.locationRepository.trayMovements(id).find(filter);
  }

  @post('/locations/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'Location model instance',
        content: {'application/json': {schema: getModelSchemaRef(TrayMovement)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Location.prototype.location_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {
            title: 'NewTrayMovementInLocation',
            exclude: ['tray_movement_id'],
            optional: ['locationId']
          }),
        },
      },
    }) trayMovement: Omit<TrayMovement, 'tray_movement_id'>,
  ): Promise<TrayMovement> {
    return this.locationRepository.trayMovements(id).create(trayMovement);
  }

  @patch('/locations/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'Location.TrayMovement PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {partial: true}),
        },
      },
    })
    trayMovement: Partial<TrayMovement>,
    @param.query.object('where', getWhereSchemaFor(TrayMovement)) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.locationRepository.trayMovements(id).patch(trayMovement, where);
  }

  @del('/locations/{id}/tray-movements', {
    responses: {
      '200': {
        description: 'Location.TrayMovement DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(TrayMovement)) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.locationRepository.trayMovements(id).delete(where);
  }
}
