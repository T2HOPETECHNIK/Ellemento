import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {ActionType, ActionTypeRelations} from '../models';

export class ActionTypeRepository extends DefaultCrudRepository<
  ActionType,
  typeof ActionType.prototype.action_type_id,
  ActionTypeRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(ActionType, dataSource);
  }
}
