import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, BelongsToAccessor, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Stage, StageRelations, Tray, StateWorkflow} from '../models';
import {TrayRepository} from './tray.repository';
import {StateWorkflowRepository} from './state-workflow.repository';

export class StageRepository extends DefaultCrudRepository<
  Stage,
  typeof Stage.prototype.stage_id,
  StageRelations
> {

  public readonly stage_id_tray: BelongsToAccessor<Tray, typeof Stage.prototype.stage_id>;

  public readonly stateWorkflows: HasManyRepositoryFactory<StateWorkflow, typeof Stage.prototype.stage_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('TrayRepository') protected trayRepositoryGetter: Getter<TrayRepository>, @repository.getter('StateWorkflowRepository') protected stateWorkflowRepositoryGetter: Getter<StateWorkflowRepository>,
  ) {
    super(Stage, dataSource);
    this.stateWorkflows = this.createHasManyRepositoryFactoryFor('stateWorkflows', stateWorkflowRepositoryGetter,);
    this.registerInclusionResolver('stateWorkflows', this.stateWorkflows.inclusionResolver);
    this.stage_id_tray = this.createBelongsToAccessorFor('stage_id_tray', trayRepositoryGetter,);
    this.registerInclusionResolver('stage_id_tray', this.stage_id_tray.inclusionResolver);
  }
}
