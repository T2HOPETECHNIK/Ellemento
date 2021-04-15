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
  TrayType,
  Stage,
} from '../models';
import {TrayTypeRepository} from '../repositories';

export class TrayTypeStageController {
  constructor(
    @repository(TrayTypeRepository) protected trayTypeRepository: TrayTypeRepository,
  ) { }

  @get('/tray-types/{id}/stages', {
    responses: {
      '200': {
        description: 'Array of TrayType has many Stage',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Stage)},
          },
        },
      },
    },
  })
  async find(
    @param.path.number('id') id: number,
    @param.query.object('filter') filter?: Filter<Stage>,
  ): Promise<Stage[]> {
    return this.trayTypeRepository.stages(id).find(filter);
  }

  @post('/tray-types/{id}/stages', {
    responses: {
      '200': {
        description: 'TrayType model instance',
        content: {'application/json': {schema: getModelSchemaRef(Stage)}},
      },
    },
  })
  async create(
    @param.path.number('id') id: typeof TrayType.prototype.tray_type_id,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Stage, {
            title: 'NewStageInTrayType',
            exclude: ['stage_id'],
            optional: ['trayTypeId']
          }),
        },
      },
    }) stage: Omit<Stage, 'stage_id'>,
  ): Promise<Stage> {
    return this.trayTypeRepository.stages(id).create(stage);
  }

  @patch('/tray-types/{id}/stages', {
    responses: {
      '200': {
        description: 'TrayType.Stage PATCH success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async patch(
    @param.path.number('id') id: number,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Stage, {partial: true}),
        },
      },
    })
    stage: Partial<Stage>,
    @param.query.object('where', getWhereSchemaFor(Stage)) where?: Where<Stage>,
  ): Promise<Count> {
    return this.trayTypeRepository.stages(id).patch(stage, where);
  }

  @del('/tray-types/{id}/stages', {
    responses: {
      '200': {
        description: 'TrayType.Stage DELETE success count',
        content: {'application/json': {schema: CountSchema}},
      },
    },
  })
  async delete(
    @param.path.number('id') id: number,
    @param.query.object('where', getWhereSchemaFor(Stage)) where?: Where<Stage>,
  ): Promise<Count> {
    return this.trayTypeRepository.stages(id).delete(where);
  }
}
