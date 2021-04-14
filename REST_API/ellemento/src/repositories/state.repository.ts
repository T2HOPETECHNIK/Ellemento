import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {State, StateRelations} from '../models';

export class StateRepository extends DefaultCrudRepository<
  State,
  typeof State.prototype.state_id,
  StateRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(State, dataSource);
  }
}
