import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {StateWorkflow, StateWorkflowRelations} from '../models';

export class StateWorkflowRepository extends DefaultCrudRepository<
  StateWorkflow,
  typeof StateWorkflow.prototype.state_type_id,
  StateWorkflowRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(StateWorkflow, dataSource);
  }
}
