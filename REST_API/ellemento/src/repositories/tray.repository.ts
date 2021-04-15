import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Tray, TrayRelations} from '../models';

export class TrayRepository extends DefaultCrudRepository<
  Tray,
  typeof Tray.prototype.tray_id,
  TrayRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(Tray, dataSource);
  }
}
