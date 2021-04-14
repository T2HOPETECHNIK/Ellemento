import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {LightHistory, LightHistoryRelations} from '../models';

export class LightHistoryRepository extends DefaultCrudRepository<
  LightHistory,
  typeof LightHistory.prototype.light_history_id,
  LightHistoryRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(LightHistory, dataSource);
  }
}
