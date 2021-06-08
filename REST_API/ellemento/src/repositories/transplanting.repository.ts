import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Transplanting, TransplantingRelations} from '../models';

export class TransplantingRepository extends DefaultCrudRepository<
  Transplanting,
  typeof Transplanting.prototype.id,
  TransplantingRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(Transplanting, dataSource);
  }
}
