import {
  Count,
  CountSchema,
  Filter,
  FilterExcludingWhere,
  repository,
  Where,
} from '@loopback/repository';
import {
  post,
  param,
  get,
  getModelSchemaRef,
  patch,
  put,
  del,
  requestBody,
  response,
} from '@loopback/rest';
import {LocationStageAssignment} from '../models';
import {LocationStageAssignmentRepository} from '../repositories';

export class EllementoLocationStageAssignmentController {
  constructor(
    @repository(LocationStageAssignmentRepository)
    public locationStageAssignmentRepository : LocationStageAssignmentRepository,
  ) {}

  @post('/location-stage-assignments')
  @response(200, {
    description: 'LocationStageAssignment model instance',
    content: {'application/json': {schema: getModelSchemaRef(LocationStageAssignment)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LocationStageAssignment, {
            title: 'NewLocationStageAssignment',
            exclude: ['id'],
          }),
        },
      },
    })
    locationStageAssignment: Omit<LocationStageAssignment, 'id'>,
  ): Promise<LocationStageAssignment> {
    return this.locationStageAssignmentRepository.create(locationStageAssignment);
  }

  @get('/location-stage-assignments/count')
  @response(200, {
    description: 'LocationStageAssignment model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(LocationStageAssignment) where?: Where<LocationStageAssignment>,
  ): Promise<Count> {
    return this.locationStageAssignmentRepository.count(where);
  }

  @get('/location-stage-assignments')
  @response(200, {
    description: 'Array of LocationStageAssignment model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(LocationStageAssignment, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(LocationStageAssignment) filter?: Filter<LocationStageAssignment>,
  ): Promise<LocationStageAssignment[]> {
    return this.locationStageAssignmentRepository.find(filter);
  }

  @patch('/location-stage-assignments')
  @response(200, {
    description: 'LocationStageAssignment PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LocationStageAssignment, {partial: true}),
        },
      },
    })
    locationStageAssignment: LocationStageAssignment,
    @param.where(LocationStageAssignment) where?: Where<LocationStageAssignment>,
  ): Promise<Count> {
    return this.locationStageAssignmentRepository.updateAll(locationStageAssignment, where);
  }

  @get('/location-stage-assignments/{id}')
  @response(200, {
    description: 'LocationStageAssignment model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(LocationStageAssignment, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(LocationStageAssignment, {exclude: 'where'}) filter?: FilterExcludingWhere<LocationStageAssignment>
  ): Promise<LocationStageAssignment> {
    return this.locationStageAssignmentRepository.findById(id, filter);
  }

  @patch('/location-stage-assignments/{id}')
  @response(204, {
    description: 'LocationStageAssignment PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(LocationStageAssignment, {partial: true}),
        },
      },
    })
    locationStageAssignment: LocationStageAssignment,
  ): Promise<void> {
    await this.locationStageAssignmentRepository.updateById(id, locationStageAssignment);
  }

  @put('/location-stage-assignments/{id}')
  @response(204, {
    description: 'LocationStageAssignment PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() locationStageAssignment: LocationStageAssignment,
  ): Promise<void> {
    await this.locationStageAssignmentRepository.replaceById(id, locationStageAssignment);
  }

  @del('/location-stage-assignments/{id}')
  @response(204, {
    description: 'LocationStageAssignment DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.locationStageAssignmentRepository.deleteById(id);
  }
}
