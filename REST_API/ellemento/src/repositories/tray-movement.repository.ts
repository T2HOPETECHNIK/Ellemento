import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {TrayMovement, TrayMovementRelations} from '../models';

export class TrayMovementRepository extends DefaultCrudRepository<
  TrayMovement,
  typeof TrayMovement.prototype.tray_movement_id,
  TrayMovementRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(TrayMovement, dataSource);
  }
}
