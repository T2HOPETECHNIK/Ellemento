import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {History, HistoryRelations} from '../models';

export class HistoryRepository extends DefaultCrudRepository<
  History,
  typeof History.prototype.history_id,
  HistoryRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(History, dataSource);
  }
}
