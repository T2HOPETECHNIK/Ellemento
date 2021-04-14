import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {TrayType, TrayTypeRelations} from '../models';

export class TrayTypeRepository extends DefaultCrudRepository<
  TrayType,
  typeof TrayType.prototype.tray_type_id,
  TrayTypeRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(TrayType, dataSource);
  }
}
