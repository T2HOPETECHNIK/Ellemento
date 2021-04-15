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
import {Tray} from '../models';
import {TrayRepository} from '../repositories';

export class EllementoTrayController {
  constructor(
    @repository(TrayRepository)
    public trayRepository : TrayRepository,
  ) {}

  @post('/trays')
  @response(200, {
    description: 'Tray model instance',
    content: {'application/json': {schema: getModelSchemaRef(Tray)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Tray, {
            title: 'NewTray',
            exclude: ['id'],
          }),
        },
      },
    })
    tray: Omit<Tray, 'id'>,
  ): Promise<Tray> {
    return this.trayRepository.create(tray);
  }

  @get('/trays/count')
  @response(200, {
    description: 'Tray model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(Tray) where?: Where<Tray>,
  ): Promise<Count> {
    return this.trayRepository.count(where);
  }

  @get('/trays')
  @response(200, {
    description: 'Array of Tray model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(Tray, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(Tray) filter?: Filter<Tray>,
  ): Promise<Tray[]> {
    return this.trayRepository.find(filter);
  }

  @patch('/trays')
  @response(200, {
    description: 'Tray PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Tray, {partial: true}),
        },
      },
    })
    tray: Tray,
    @param.where(Tray) where?: Where<Tray>,
  ): Promise<Count> {
    return this.trayRepository.updateAll(tray, where);
  }

  @get('/trays/{id}')
  @response(200, {
    description: 'Tray model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(Tray, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(Tray, {exclude: 'where'}) filter?: FilterExcludingWhere<Tray>
  ): Promise<Tray> {
    return this.trayRepository.findById(id, filter);
  }

  @patch('/trays/{id}')
  @response(204, {
    description: 'Tray PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Tray, {partial: true}),
        },
      },
    })
    tray: Tray,
  ): Promise<void> {
    await this.trayRepository.updateById(id, tray);
  }

  @put('/trays/{id}')
  @response(204, {
    description: 'Tray PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() tray: Tray,
  ): Promise<void> {
    await this.trayRepository.replaceById(id, tray);
  }

  @del('/trays/{id}')
  @response(204, {
    description: 'Tray DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.trayRepository.deleteById(id);
  }
}
