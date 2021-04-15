import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {ActionType, ActionTypeRelations, StateWorkflow} from '../models';
import {StateWorkflowRepository} from './state-workflow.repository';

export class ActionTypeRepository extends DefaultCrudRepository<
  ActionType,
  typeof ActionType.prototype.action_type_id,
  ActionTypeRelations
> {

  public readonly stateWorkflows: HasManyRepositoryFactory<StateWorkflow, typeof ActionType.prototype.action_type_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('StateWorkflowRepository') protected stateWorkflowRepositoryGetter: Getter<StateWorkflowRepository>,
  ) {
    super(ActionType, dataSource);
    this.stateWorkflows = this.createHasManyRepositoryFactoryFor('stateWorkflows', stateWorkflowRepositoryGetter,);
    this.registerInclusionResolver('stateWorkflows', this.stateWorkflows.inclusionResolver);
  }
}
