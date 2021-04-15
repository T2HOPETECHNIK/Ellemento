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
import {TrayType} from '../models';
import {TrayTypeRepository} from '../repositories';

export class EllementoTrayTypeController {
  constructor(
    @repository(TrayTypeRepository)
    public trayTypeRepository : TrayTypeRepository,
  ) {}

  @post('/tray-types')
  @response(200, {
    description: 'TrayType model instance',
    content: {'application/json': {schema: getModelSchemaRef(TrayType)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayType, {
            title: 'NewTrayType',
            exclude: ['id'],
          }),
        },
      },
    })
    trayType: Omit<TrayType, 'id'>,
  ): Promise<TrayType> {
    return this.trayTypeRepository.create(trayType);
  }

  @get('/tray-types/count')
  @response(200, {
    description: 'TrayType model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(TrayType) where?: Where<TrayType>,
  ): Promise<Count> {
    return this.trayTypeRepository.count(where);
  }

  @get('/tray-types')
  @response(200, {
    description: 'Array of TrayType model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(TrayType, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(TrayType) filter?: Filter<TrayType>,
  ): Promise<TrayType[]> {
    return this.trayTypeRepository.find(filter);
  }

  @patch('/tray-types')
  @response(200, {
    description: 'TrayType PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayType, {partial: true}),
        },
      },
    })
    trayType: TrayType,
    @param.where(TrayType) where?: Where<TrayType>,
  ): Promise<Count> {
    return this.trayTypeRepository.updateAll(trayType, where);
  }

  @get('/tray-types/{id}')
  @response(200, {
    description: 'TrayType model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(TrayType, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.number('id') id: number,
    @param.filter(TrayType, {exclude: 'where'}) filter?: FilterExcludingWhere<TrayType>
  ): Promise<TrayType> {
    return this.trayTypeRepository.findById(id, filter);
  }

  @patch('/tray-types/{id}')
  @response(204, {
    description: 'TrayType PATCH success',
  })
  async updateById(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(TrayType, {partial: true}),
        },
      },
    })
    trayType: TrayType,
  ): Promise<void> {
    await this.trayTypeRepository.updateById(id, trayType);
  }

  @put('/tray-types/{id}')
  @response(204, {
    description: 'TrayType PUT success',
  })
  async replaceById(
    @param.path.number('id') id: number,
    @requestBody() trayType: TrayType,
  ): Promise<void> {
    await this.trayTypeRepository.replaceById(id, trayType);
  }

  @del('/tray-types/{id}')
  @response(204, {
    description: 'TrayType DELETE success',
  })
  async deleteById(@param.path.number('id') id: number): Promise<void> {
    await this.trayTypeRepository.deleteById(id);
  }
}
