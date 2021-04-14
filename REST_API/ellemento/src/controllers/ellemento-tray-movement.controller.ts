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
import {TrayMovement} from '../models';
import {TrayMovementRepository} from '../repositories';

export class EllementoTrayMovementController {
  constructor(
    @repository(TrayMovementRepository)
    public trayMovementRepository : TrayMovementRepository,
  ) {}

  @post('/tray-movements')
  @response(200, {
    description: 'TrayMovement model instance',
    content: {'application/json': {schema: getModelSchemaRef(TrayMovement)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {
            title: 'NewTrayMovement',
            exclude: ['id'],
          }),
        },
      },
    })
    trayMovement: Omit<TrayMovement, 'id'>,
  ): Promise<TrayMovement> {
    return this.trayMovementRepository.create(trayMovement);
  }

  @get('/tray-movements/count')
  @response(200, {
    description: 'TrayMovement model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(TrayMovement) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.trayMovementRepository.count(where);
  }

  @get('/tray-movements')
  @response(200, {
    description: 'Array of TrayMovement model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(TrayMovement, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(TrayMovement) filter?: Filter<TrayMovement>,
  ): Promise<TrayMovement[]> {
    return this.trayMovementRepository.find(filter);
  }

  @patch('/tray-movements')
  @response(200, {
    description: 'TrayMovement PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {partial: true}),
        },
      },
    })
    trayMovement: TrayMovement,
    @param.where(TrayMovement) where?: Where<TrayMovement>,
  ): Promise<Count> {
    return this.trayMovementRepository.updateAll(trayMovement, where);
  }

  @get('/tray-movements/{id}')
  @response(200, {
    description: 'TrayMovement model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(TrayMovement, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(TrayMovement, {exclude: 'where'}) filter?: FilterExcludingWhere<TrayMovement>
  ): Promise<TrayMovement> {
    return this.trayMovementRepository.findById(id, filter);
  }

  @patch('/tray-movements/{id}')
  @response(204, {
    description: 'TrayMovement PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayMovement, {partial: true}),
        },
      },
    })
    trayMovement: TrayMovement,
  ): Promise<void> {
    await this.trayMovementRepository.updateById(id, trayMovement);
  }

  @put('/tray-movements/{id}')
  @response(204, {
    description: 'TrayMovement PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() trayMovement: TrayMovement,
  ): Promise<void> {
    await this.trayMovementRepository.replaceById(id, trayMovement);
  }

  @del('/tray-movements/{id}')
  @response(204, {
    description: 'TrayMovement DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.trayMovementRepository.deleteById(id);
  }
}
