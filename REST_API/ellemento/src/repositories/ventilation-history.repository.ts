import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {VentilationHistory, VentilationHistoryRelations} from '../models';

export class VentilationHistoryRepository extends DefaultCrudRepository<
  VentilationHistory,
  typeof VentilationHistory.prototype.ventilation_history_id,
  VentilationHistoryRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(VentilationHistory, dataSource);
  }
}
