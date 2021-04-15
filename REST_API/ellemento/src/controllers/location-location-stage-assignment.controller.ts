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
  LocationStageAssignment,
} from '../models';
import {LocationRepository} from '../repositories';

export class LocationLocationStageAssignmentController {
  constructor(
    @repository(LocationRepository) protected locationRepository: LocationRepository,
  ) { }

  @get('/locations/{id}/location-stage-assignments', {
    responses: {
      '200': {
        description: 'Array of Location has many LocationStageAssignment',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(LocationStageAssignment)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<LocationStageAssignment>,
  ): Promise<LocationStageAssignment[]> {
    return this.locationRepository.locationStageAssignments(id).find(filter);
  }

  @post('/locations/{id}/location-stage-assignments', {
    responses: {
      '200': {
        description: 'Location model instance',
        content: {'application/json': {schema: getModelSchemaRef(LocationStageAssignment)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof Location.prototype.location_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LocationStageAssignment, {
            title: 'NewLocationStageAssignmentInLocation',
            exclude: ['location_stage_assignment_id'],
            optional: ['locationId']
          }),
        },
      },
    }) locationStageAssignment: Omit<LocationStageAssignment, 'location_stage_assignment_id'>,
  ): Promise<LocationStageAssignment> {
    return this.locationRepository.locationStageAssignments(id).create(locationStageAssignment);
  }

  @patch('/locations/{id}/location-stage-assignments', {
    responses: {
      '200': {
        description: 'Location.LocationStageAssignment PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LocationStageAssignment, {partial: true}),
        },
      },
    })
    locationStageAssignment: Partial<LocationStageAssignment>,
    @param.query.object('where', getWhereSchemaFor(LocationStageAssignment)) where?: Where<LocationStageAssignment>,
  ): Promise<Count> {
    return this.locationRepository.locationStageAssignments(id).patch(locationStageAssignment, where);
  }

  @del('/locations/{id}/location-stage-assignments', {
    responses: {
      '200': {
        description: 'Location.LocationStageAssignment DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(LocationStageAssignment)) where?: Where<LocationStageAssignment>,
  ): Promise<Count> {
    return this.locationRepository.locationStageAssignments(id).delete(where);
  }
}
