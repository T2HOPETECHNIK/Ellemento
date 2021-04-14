import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Batch, BatchRelations} from '../models';

export class BatchRepository extends DefaultCrudRepository<
  Batch,
  typeof Batch.prototype.batch_id,
  BatchRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(Batch, dataSource);
  }
}
