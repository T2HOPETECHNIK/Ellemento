import {
  repository,
} from '@loopback/repository';
import {
  param,
  get,
  getModelSchemaRef,
} from '@loopback/rest';
import {
  Stage,
  Tray,
} from '../models';
import {StageRepository} from '../repositories';

export class StageTrayController {
  constructor(
    @repository(StageRepository)
    public stageRepository: StageRepository,
  ) { }

  @get('/stages/{id}/tray', {
    responses: {
      '200': {
        description: 'Tray belonging to Stage',
        content: {
          'application/json': {
            schema: {type: 'array', items: getModelSchemaRef(Tray)},
          },
        },
      },
    },
  })
  async getTray(
    @param.path.number('id') id: typeof Stage.prototype.stage_id,
  ): Promise<Tray> {
    return this.stageRepository.stage_id_tray(id);
  }
}
