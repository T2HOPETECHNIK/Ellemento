import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {StateWorkflow, StateWorkflowRelations, State} from '../models';
import {StateRepository} from './state.repository';

export class StateWorkflowRepository extends DefaultCrudRepository<
  StateWorkflow,
  typeof StateWorkflow.prototype.state_type_id,
  StateWorkflowRelations
> {

  public readonly states: HasManyRepositoryFactory<State, typeof StateWorkflow.prototype.state_type_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('StateRepository') protected stateRepositoryGetter: Getter<StateRepository>,
  ) {
    super(StateWorkflow, dataSource);
    this.states = this.createHasManyRepositoryFactoryFor('states', stateRepositoryGetter,);
    this.registerInclusionResolver('states', this.states.inclusionResolver);
  }
}
