import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasOneRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Condition, ConditionRelations, StateWorkflow} from '../models';
import {StateWorkflowRepository} from './state-workflow.repository';

export class ConditionRepository extends DefaultCrudRepository<
  Condition,
  typeof Condition.prototype.condition_id,
  ConditionRelations
> {

  public readonly stateWorkflow: HasOneRepositoryFactory<StateWorkflow, typeof Condition.prototype.condition_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('StateWorkflowRepository') protected stateWorkflowRepositoryGetter: Getter<StateWorkflowRepository>,
  ) {
    super(Condition, dataSource);
    this.stateWorkflow = this.createHasOneRepositoryFactoryFor('stateWorkflow', stateWorkflowRepositoryGetter);
    this.registerInclusionResolver('stateWorkflow', this.stateWorkflow.inclusionResolver);
  }
}
