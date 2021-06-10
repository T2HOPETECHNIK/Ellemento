import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {TrayWashing, TrayWashingRelations} from '../models';

export class TrayWashingRepository extends DefaultCrudRepository<
  TrayWashing,
  typeof TrayWashing.prototype.id,
  TrayWashingRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(TrayWashing, dataSource);
  }
}
