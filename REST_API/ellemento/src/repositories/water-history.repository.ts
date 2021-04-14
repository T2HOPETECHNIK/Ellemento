import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {WaterHistory, WaterHistoryRelations} from '../models';

export class WaterHistoryRepository extends DefaultCrudRepository<
  WaterHistory,
  typeof WaterHistory.prototype.water_history_id,
  WaterHistoryRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(WaterHistory, dataSource);
  }
}
