import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Potting, PottingRelations} from '../models';

export class PottingRepository extends DefaultCrudRepository<
  Potting,
  typeof Potting.prototype.tray_action_table_id,
  PottingRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(Potting, dataSource);
  }
}
